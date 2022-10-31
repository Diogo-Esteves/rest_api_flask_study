# rest_api_flask_study

Using this repo to study

## Run locally

```sh
flask run
```

## Run locally with docker

Running the container with -w and -v makes the server to restart always the code was updated.

```sh
docker build -t rest-api-flask .
docker container run -p 5000:5000 -w /app -v "$(pwd):/app" rest-api-flask
```

## To run the tests

```sh
python -m unittest
```

## Flask commands with Alembic

Generating migration files into the db.

```sh
flask db init
flask db migrate
flask db upgrade
```
