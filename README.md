# Sharif Star

Simple Django project for evaluation.


## Prerequisite
 - Python installation.
 - [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Development Guide

1. Clone repository.

2. Launch virtualenv shell:
```bash
$ source bin/activate
```

3. Install requirement dependencies:
```bash
$ pip install -r requirements.txt
```

4. Migrate database (sqlite)
```bash
(sharifstar) $ ./manage.py migrate
```

7. Runserver
```bash
(sharifstar) $ ./manage.py runserver
```