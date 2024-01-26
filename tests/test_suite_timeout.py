pytest_plugins = "pytester",


def test_no_timeout(pytester):
    pytester.makepyfile("""
        import pytest
        
        @pytest.mark.parametrize('i', range(10)) 
        def test_fast(i):
           ...
    """)
    result = pytester.runpytest()
    result.assert_outcomes(passed=10)


def test_timeout(pytester):
    pytester.makepyfile("""
        import time
        import pytest
       
        @pytest.mark.parametrize('i', range(10)) 
        def test_slow(i):
            time.sleep(1)
    """)
    result = pytester.runpytest('--suite-timeout', '0.5')
    result.stdout.fnmatch_lines([
        '*!! suite-timeout: 0.5 sec exceeded !!*',
    ])
    outcomes = result.parseoutcomes()
    assert outcomes['passed'] == 1
