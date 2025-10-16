# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to [Semantic Versioning].

## [Unreleased]

### Fixed

- Fixed deprecation of store_const being used as a positional argument

## [3.2.2] - 2025-01-14

### Fixed

- Fixed dvenv

## [3.2.1] - 2025-01-14

### Fixed

- Fixed unsetting env vars
- Fixed activating venv with env vars

## [3.2.0] - 2025-01-13

### Added

- Export `UV_PROJECT_ENVIRONMENT` to help using uv

## [3.1.0] - 2025-01-06

### Added

- Allow choosing seed type

## [3.0.0] - 2025-01-05

### Changed

- Informative printing is handled by dry_run and verbosity
- Use uv for creating venvs

### Fixed

- Fixed an env var that couldn't be handled by windows
- Fixed the minimum python version is set to 3.9
- Fixed the path in pvenv init

## [2.0.0] - 2024-07-23

### Changed

- Dropped python 3.8 support
- Changed license to BSD 3-Clause

## [1.0.0] - 2023-03-10

### Fixed

- Fixed the bug with unprintable help in subcommands

### Removed

- Dropped python 3.7 support

## [0.6.0] - 2022-11-23

### Added

- Allow overriding env vars with a .d directory

### Fixed

- Unset completely the new env vars

## [0.5.0] - 2022-11-22

### Fixed

- Fixed `avenv` with multiple environment variables

## [0.4.0] - 2022-11-18

### Fixed

- Fixed setting the project path when using `mkvenv`

## [0.3.1] - 2022-11-17

### Fixed

- Fixed error messages when using `mkvenv`

## [0.3.0] - 2022-11-17

### Added

- Added `rmvenv` to remove existing virtual environments
- Added `mkvenv` to create virtual environments
- Added `avenv` to activate virtual environments
- Added `dvenv` to deactivate virtual environments

## [0.2.0] - 2022-11-14

### Added

- Added `invenv` to source environment variables
- Added `outvenv` to remove sourced environment variables with `invenv`

## [0.1.0] - 2022-11-13

### Added

- Added `lsvenv` to list all the available virtual environments

[Keep a Changelog]: https://keepachangelog.com/en/1.1.0/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
[Unreleased]: https://github.com/spapanik/pvenv/compare/v3.2.2...main
[3.2.2]: https://github.com/spapanik/pvenv/compare/v3.2.1...v3.2.2
[3.2.1]: https://github.com/spapanik/pvenv/compare/v3.2.0...v3.2.1
[3.2.0]: https://github.com/spapanik/pvenv/compare/v3.1.0...v3.2.0
[3.1.0]: https://github.com/spapanik/pvenv/compare/v3.0.0...v3.1.0
[3.0.0]: https://github.com/spapanik/pvenv/compare/v2.0.0...v3.0.0
[2.0.0]: https://github.com/spapanik/pvenv/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/spapanik/pvenv/compare/v0.6.0...v1.0.0
[0.6.0]: https://github.com/spapanik/pvenv/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/spapanik/pvenv/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/spapanik/pvenv/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/spapanik/pvenv/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/spapanik/pvenv/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/spapanik/pvenv/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/spapanik/yamk/releases/tag/v0.1.0
