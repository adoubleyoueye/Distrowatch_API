# distrowatch_api app

[![run linter](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/lint.yml/badge.svg)](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/lint.yml)
[![run tests](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/test.yml/badge.svg)](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/test.yml)
[![.github/workflows/deploy.yml](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/deploy.yml/badge.svg?branch=master)](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/deploy.yml)

### Run the app in terminal

1. Start a Postgres database server on your machine or in the cloud.
2. Set the following environment variables in your terminal.

```
export POSTGRES_HOST=<address-where-database-running>
export POSTGRES_PORT=<port-where-database-running>
export POSTGRES_DB=<database-name>
export POSTGRES_USER=<username-for-database>
export POSTGRES_PASSWORD=<password-to-database>
```

3. Install packages and start the application server.

```
$ make install
$ make migrate
$ make run
```

### Make API calls against the server

1. Go to [http://localhost:8000/swagger](http://localhost:8000/swagger) to see Swagger documentation for API endpoints.
2. Run the APIs by clicking the "Try it now" button on the Swagger page.


### Run tests and check code coverage

```
$ make test
$ make coverage
```

### Lint your code

```
$ make lint
```
