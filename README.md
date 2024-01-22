# pytest-suite-timeout

A pytest plugin for ensuring max suite time.

Really though, it's: if the timeout expires, no new tests are started.

----

## Installation

From PyPI:

```
$ pip install pytest-suite-timeout
```

## Usage


Specify the max suite time with `--suite-timeout`, in minutes (float).

Example of max 1.5 minutes:

```
$ pytest --suite-timeout=1.5 
```

## Defaults to no timeout

If you don't pass in `--suite-timeout`, nothing happens.

## Timeout behavior

Timeout is done between tests. 
If a timeout is noticed, `pytest.exit()` is called, stopping all further testing.

## Contributing

Contributions are welcome. Tests can be run with [tox](https://tox.readthedocs.io/en/latest/).
Test coverage is now 100%. Please make sure to keep it at 100%.
If you have an awesome pull request and need help with getting coverage back up, let me know.


## License

Distributed under the terms of the [MIT](http://opensource.org/licenses/MIT) license, "pytest-suite-timeout" is free and open source software

## Issues

If you encounter any problems, please [file an issue](https://github.com/okken/pytest-suite-timeout/issues) along with a detailed description.

## Changelog

See [changelog.md](https://github.com/okken/pytest-suite-timeout/blob/main/changelog.md)