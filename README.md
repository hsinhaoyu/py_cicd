[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=hsinhaoyu_py_cicd&metric=coverage)](https://sonarcloud.io/summary/new_code?id=hsinhaoyu_py_cicd)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=hsinhaoyu_py_cicd&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=hsinhaoyu_py_cicd)
![GitHub Actions status](https://img.shields.io/github/workflow/status/hsinhaoyu/py_cicd/Deploy)

# A minimal CI/CD setup for Python

This is just a test repo for me to experiment with CI/CD.

## Basic operations

- To install the package: `pip install -e .`
- To reformat code: `make code-format`
- To lint: `make code-lint`
- to test: `make test`

## Configuration files

#### CI/CD pipelines

- `.github/workflows`: CI/CD pipelines using [Github Actions](https://docs.github.com/en/actions)
- `Makefile`: Build scripts supporting the actions

#### Git pre-commit hooks

- `.pre-commit-config.yaml`: Config for [`pre-commit`](https://pre-commit.com)
- After checking out the repo, run `make pre-commit` or `pre-commit install` to install the hooks

#### Python dependencies ([`setuptools`](https://setuptools.pypa.io/en/latest/userguide/index.html))

- `pyproject.toml`
- `setup.py`
- `setup.cfg`

Notes:

- See [this article](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/) for more details on setuptools
- `install_requires=` in the `[options]` section of `setup.cfg` lists the files that will be installed with `pip install .` or `pip install -e .`
- The `-e` flag puts `pip install` in the _editable mode_.
- The `[options.extras_require]` section of `setup.cfg` defines a set of packages (named `dev`) that will be installed with `pip install -e .[dev]`.
