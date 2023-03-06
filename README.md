# Fask Microservice Versioning Example

[![codecov](https://codecov.io/gh/juniors90/microservice-versioning-example/branch/main/graph/badge.svg?token=XBXBOMoQUi)](https://codecov.io/gh/juniors90/microservice-versioning-example)
[![Build status](https://github.com/juniors90/microservice-versioning-example/actions/workflows/flask.yml/badge.svg)](https://github.com/juniors90/microservice-versioning-example/actions)
[![GitHub issues](https://img.shields.io/github/issues/juniors90/microservice-versioning-example)](https://github.com/juniors90/microservice-versioning-example/issues)
[![GitHub forks](https://img.shields.io/github/forks/juniors90/microservice-versioning-example)](https://github.com/juniors90/microservice-versioning-example/network)
[![GitHub stars](https://img.shields.io/github/stars/juniors90/microservice-versioning-example)](https://github.com/juniors90/microservice-versioning-example/stargazers)
[![GitHub license](https://img.shields.io/github/license/juniors90/microservice-versioning-example)](https://github.com/juniors90/microservice-versioning-example/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/juniors90/microservice-versioning-example?color=green)](https://github.com/juniors90/microservice-versioning-example/graphs/contributors)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Code built following Real Python tutorials:

- [Python REST APIs With Flask, Connexion, and SQLAlchemy – Part 1](https://realpython.com/flask-connexion-rest-api/)
- [Python REST APIs With Flask, Connexion, and SQLAlchemy – Part 2](https://realpython.com/flask-connexion-rest-api-part-2/)
- [Python REST APIs With Flask, Connexion, and SQLAlchemy – Part 3](https://realpython.com/flask-connexion-rest-api-part-3/)

Some modificationes were made:

- source code was placed in [`src`](./src/) folder instead of root folder
- docstrings in [numpydoc format](https://numpydoc.readthedocs.io/en/latest/format.html) were added
- type hints were added

For using this code, follow next steps:

1. Create an environment
2. Install project requirements:

    ```bash
    pip install -r requirements
    ```

3. Create the database:

    ```bash
    python build_database.py
    ```

4. Run the API:

    ```bash
    python -m src
    ```
