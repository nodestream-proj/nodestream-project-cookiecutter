# {{ cookiecutter.project_name }}

## Getting Started 

To get started, first install the required dependencies:

```bash
poetry install
```

Note that this project uses [poetry](https://python-poetry.org/) for dependency management. If you don't have poetry installed, you can install it following the instructions [here](https://python-poetry.org/docs/#installation).

## Development

If you don't want to keep typing `poetry run` before every command, you can run the following command to enter a shell with the correct environment:

```bash
poetry shell
```

The samples below assume you are in a poetry shell.

### Running Pipelines
To run a pipeline locally, use the following command:

```bash
nodestream run $PIPELINE_NAME 
```

### Running Tests

To run tests, use the following command:

```bash
pytest
```
