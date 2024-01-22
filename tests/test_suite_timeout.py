pytest_plugins = "pytester",


def test_no_timeout(pytester):
    pytester.makepyfile("""
        def test_fast():
           ...
    """)
    result = pytester.runpytest('--count', '10')
    result.assert_outcomes(passed=10)


def test_timeout(pytester):
    pytester.makepyfile("""
        import time
        
        def test_slow():
            time.sleep(0.1)
    """)
    result = pytester.runpytest('--count', '10', '--suite-timeout', '0.006', '-v')
    result.stdout.fnmatch_lines([
        '* suite-timeout: 0.006 minutes exceeded !!*',
    ])
    outcomes = result.parseoutcomes()
    # 0.006 * 60 = 0.36 seconds.
    # 3 will finish, then the 4th will start
    # before the 5th can be started, a timeout will be noticed
    assert outcomes['passed'] == 4
