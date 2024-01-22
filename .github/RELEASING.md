Here are the steps on how to make a new release.

Releasing is done locally, still.

1. Bump version in pyproject.toml
2. Update `CHANGELOG.md`.
3. Push the branch to `upstream`.
4. Once all tests pass, merge the PR.
5. Once the PR completes, create a Release with a new version tag on GitHub.
   Version should be in the form of "vx.y.z". ex: v0.9.2
6. `flit publish` locally.
