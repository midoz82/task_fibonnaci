# FastAPI

## Technologies
- FastApi: choosed the fastapi to create a Performance solution and have Data Validation 
- Uvicorn: Concurrency, HTTP/1.1 and WebSockets and Compatibility
- Poetry: choosed poetry for Dependency Management, Packaging and Publishing, irtual Environments and Reproducibility
- Alembic
- Pydantic: Pydantic in our project was a deliberate move to ensure robust data validation and parsing.


The architecture of the project is meticulously
automated, eliminating the need for manual loading of environment variables,
thus streamlining the setup process. This automation, coupled with a decoupled design, 
paves the way for seamless integration of emerging technologies. The decoupled nature of the infrastructure significantly 
eases the integration process, making the adaptation of new technologies a hassle-free endeavor. Such a design not only future-proofs the project but also enhances its flexibility and maintainability,
ensuring that it remains at the forefront of technological advancements.

## Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/)
* [Pyenv](https://github.com/pyenv/pyenv/)

## Local Development

* Install pyenv.

* Install python 3.9 using pyenv:

  ```bash
  pyenv install 3.9
  ```

* Install poetry

* Set python 3.9 as default

  ```bash
  pyenv global 3.9.16
  pyenv shell 3.9.16 # alternative 
  poetry env use 3.9.16 # to enforce pyenv to use the same python version
  ```


* Navigate to the project directory and install dependencies using poetry:

  ```bash
  poetry install
  ```

* to run the project from terminal

  ```bash
  poetry run uvicorn app.main:app --reload 
  ```

* docker compose will create the database for you

  ```bash
  docker-compose up
  ```

* upgrade the database:

  ```bash
  alembic upgrade head
  ```

## Local Development Using Docker Compose

You can run the environment using docker compose (it takes sometime to build and download the dependencies and start up):

```bash
docker-compose up -d
```

Open the browser and navigate to http://0.0.0.0/docs to confirm that your server is up and running.

No need to build the project again after changeing the code if you don't add a new library as a new reuirenment.
you can just restart the docker container as follows and you will have your latest changes:

```bash
docker compose restart webserver_worker
```

To check the logs, run:

```bash
docker compose logs
```

To check the logs of a specific service, add the name of the service, e.g.:

```bash
docker compose logs -f webserver_worker
```

---

## Linting and type checking

* `flake8` is used as first linter and its configuration is stored in the file `.flake8`
* `pylint` is used as second linter and its configuration is stored in the file `.pylintrc`
* `mypy` is enabled for type checking and the file `mypy.ini` contains the type checking configurations

## Formatting and sorting imports

* `autopep8` is enabled for auto formatting and its rules is in the file `.vscode/settings.json` - if you are using vscode then these rules will be applied automatically when formatting.
* `isort` is used to sort and clean the imports using the script `scripts/format-imports.sh` and you can run it  as follows:

  ```bash
  scripts/format-imports.sh
  ```
  