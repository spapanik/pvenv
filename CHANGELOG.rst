=========
Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_, and this project adheres to `Semantic Versioning`_.

`Unreleased`_
-------------

Fixed
^^^^^
* Fixed the bug with unprintable help in subcommands

Removed
^^^^^^^
* Dropped python 3.7 support

`0.6.0`_ - 2022-11-23
---------------------
Added
^^^^^
* Allow overriding env vars with a .d directory

Fixed
^^^^^
* Unset completely the new env vars

`0.5.0`_ - 2022-11-22
---------------------
Fixed
^^^^^
* Fixed `avenv` with multiple environment variables

`0.4.0`_ - 2022-11-18
---------------------
Fixed
^^^^^
* Fixed setting the project path when using `mkvenv`

`0.3.1`_ - 2022-11-17
---------------------
Fixed
^^^^^
* Fixed error messages when using `mkvenv`

`0.3.0`_ - 2022-11-17
---------------------
Added
^^^^^
* Added `rmvenv` to remove existing virtual environments
* Added `mkvenv` to create virtual environments
* Added `avenv` to activate virtual environments
* Added `dvenv` to deactivate virtual environments

`0.2.0`_ - 2022-11-14
---------------------
Added
^^^^^
* Added `invenv` to source environment variables
* Added `outvenv` to remove sourced environment variables with `invenv`

`0.1.0`_ - 2022-11-13
---------------------
Added
^^^^^
* Added `lsvenv` to list all the available virtual environments

.. _`unreleased`: https://github.com/spapanik/pvenv/compare/v0.6.0...main
.. _`0.6.0`: https://github.com/spapanik/pvenv/compare/v0.5.0...v0.6.0
.. _`0.5.0`: https://github.com/spapanik/pvenv/compare/v0.4.0...v0.5.0
.. _`0.4.0`: https://github.com/spapanik/pvenv/compare/v0.3.1...v0.4.0
.. _`0.3.1`: https://github.com/spapanik/pvenv/compare/v0.3.0...v0.3.1
.. _`0.3.0`: https://github.com/spapanik/pvenv/compare/v0.2.0...v0.3.0
.. _`0.2.0`: https://github.com/spapanik/pvenv/compare/v0.1.0...v0.2.0
.. _`0.1.0`: https://github.com/spapanik/yamk/releases/tag/v0.1.0

.. _`Keep a Changelog`: https://keepachangelog.com/en/1.0.0/
.. _`Semantic Versioning`: https://semver.org/spec/v2.0.0.html
