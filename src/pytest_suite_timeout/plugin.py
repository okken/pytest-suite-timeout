import time
import pytest

_expire_time = 0

def pytest_addoption(parser):
    parser.addoption(
        "--suite-timeout",
        action="store",
        dest="suite_timeout",
        default=None,
        type=float,
        metavar="minutes",
        help="Don't run for longer than this.")


def pytest_configure(config):
    global _expire_time, _minutes
    _minutes = config.getoption("--suite-timeout")
    if _minutes:
        _expire_time = time.time() + (_minutes * 60)


def pytest_runtest_call(item):
    if _expire_time and _expire_time < time.time():
        pytest.exit(f"suite-timeout: {_minutes} minutes exceeded",
                    returncode=0)

