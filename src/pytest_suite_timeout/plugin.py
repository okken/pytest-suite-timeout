import time
import pytest

suite_timeout_key = pytest.StashKey[float]()


SUITE_TIMEOUT_DESC = """
Timeout in seconds for entire suite.  Default is None which
means no timeout. Timeout is checked between tests, and will not interrupt a test 
in progress. Can be specified as a float.
"""

def pytest_addoption(parser):
    parser.addoption(
        "--suite-timeout",
        action="store",
        dest="suite_timeout",
        default=None,
        type=float,
        metavar="SECONDS",
        help=SUITE_TIMEOUT_DESC)


def pytest_configure(config):
    timeout = config.getoption("--suite-timeout")
    if timeout is not None:
        expire_time = time.time() + timeout
    else:
        expire_time = 0
    config.stash[suite_timeout_key] = expire_time


def pytest_runtest_makereport(item, call):
    session = item.session
    config = session.config
    expire_time = config.stash[suite_timeout_key]
    if expire_time and (expire_time < time.time()):
        timeout = config.getoption("--suite-timeout")
        session.shouldfail = f"suite-timeout: {timeout} sec exceeded"
