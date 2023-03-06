# Fask Microservice Versioning Example

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
