# Changelog

All notable changes to this project  be documented in this file.

<!--

## [Unreleased] - yyyy-month-dd

### Added

- nothing so far

### Fixed

- nothing so far

### Changed

- nothing so far

-->

## [0.1.0] - 2024-Jan-26

### Modified
- Changed timeout to seconds instead of minutes.
  - This matches other timeout utilities and matches `time.time()` units.
- Move the timeout to `pytest_runtest_makereport()`
- Changed exit strategy from `pytest.exit()` to `session.shouldfail`
- Moved module global variables to `config.stash`
- Thanks to some help from Florian (via pytest-timeout merge discussion)

## [0.0.2] - 2024-Jan-21

### Modified
- Move the timeout to `pytest_runtest_logfinish()`
    - Seems to behave more as expected, not starting the next test.

## [0.0.1] - 2024-Jan-21

### Added
- Everything
    - Initial version
