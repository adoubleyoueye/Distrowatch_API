<h1 align="center">DistroWatch API :penguin:</h1>

[![run linter](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/lint.yml/badge.svg)](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/lint.yml)
[![run tests](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/test.yml/badge.svg)](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/test.yml)
[![.github/workflows/deploy.yml](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/deploy.yml/badge.svg?branch=master)](https://github.com/adoubleyoueye/Distrowatch_API/actions/workflows/deploy.yml)

### :dart: About ###

*[DistroWatch](https://distrowatch.com/) API* is a JSON API which provides basic information about Linux distributions as well as other free software/open source Unix-like operating systems. As you may know, there are literally dozens if not hundreds of Linux distributions.

I created this project because Linux is life. I got started with Linux in 2018. I grew to love it for more reasons than "it's not Windows".

My distro of choice for desktop computing is Fedora xfce.

### :triangular_ruler: Technologies ###

- Django
- Django Rest Framework
- Postgresql


### Usage 

#### [Documentation Link](https://distrowatch-api.herokuapp.com/swagger/)


Retrieve information about a specific distrobution in JSON format.

```curl -X GET "https://distrowatch-api.herokuapp.com/distro/17/" -H  "accept: application/json"``` 

Example response:
```json
  {
    "id": 17,
    "name": "Baruwa Enterprise Edition",
    "description": "Baruwa Enterprise Edition is a CentOS-based, commercial Linux distribution delivering fully-fledged mail security solutions. It provides protection from spam, viruses, phishing attempts and malware. It is designed for organizations of any size from small to medium businesses to large service providers, carriers and enterprises. Baruwa Enterprise Edition works with any standard SMTP server and it comes with automated installation and configuration management tools. The web-based management interface is implemented using web 2.0 features (AJAX) and available in over 25 languages. Also included is reporting functionality with an easy-to-use query builder and advanced search options.",
    "logo": null,
    "price": 0,
    "os_type": "LINUX",
    "origin": "South Africa",
    "based_on": "Fedora, CentOS",
    "category": null,
    "status": "ACTIVE",
    "popularity": 239,
    "home_page": "https://www.baruwa.com/",
    "user_forums": "--",
    "desktop_interfaces": [],
    "architectures": [
      "x86_64"
    ]
  }
```

### :runner: Local install

#### Run the app in terminal

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

#### Make API calls against the server

1. Go to [http://localhost:8000/swagger](http://localhost:8000/swagger) to see Swagger documentation for API endpoints.
2. Run the APIs by clicking the "Try it now" button on the Swagger page.


#### Run tests and check code coverage

```
$ make test
$ make coverage
```

#### Lint your code

```
$ make lint
```

### Resources
- Data sourced from [DistroWatch](https://distrowatch.com/). 


