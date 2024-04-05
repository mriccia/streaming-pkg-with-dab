# streaming-pkg-with-dab


## Dev setup


1. Ensure you have Python 3.10 and `hatch` installed.
2. Create a new environment with `hatch`:

```
hatch env create
```

3. Activate the environment in VS Code:

```
hatch run python -c "import sys; print(sys.executable)" # set the output to VS Code interpreter
```

4. Install the package and environment:

```
hatch run sync
```

## CI/CD setup

1. Install Databricks CLI
2. Set up a Databricks profile with the CLI:

```
databricks auth login -p streaming-pkg-demo --host <workspace-url>
```