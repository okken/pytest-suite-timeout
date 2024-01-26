"""
Mostly for an example.
Try with : --suite-timeout=1.5
"""
import time
import pytest

@pytest.mark.parametrize("i", range(2))
def test_slow(i):
    time.sleep(1)
