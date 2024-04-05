# streaming-pkg-with-dab

This is an example package with several Databricks jobs that demonstrate how to use a Python package with Databricks and Databricks Asset Bundles.

## Dev setup on local machine


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

3. To deploy the jobs to the dev environment, run:

```
databricks bundle deploy -t dev
```

4. To deploy the jobs to the prod environment, run:

```
databricks bundle deploy -t prod
```