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

5. Create Staff User (sqlite)
```bash
(sharifstar) $ ./manage.py createsuperuser
```

6. Runserver
```bash
(sharifstar) $ ./manage.py runserver
```
## Usage
###### Authentication
- Sign in page (required for accessing to the profile page)
> [localhost:8000/accounts/login]()
- Sign Up page
> [localhost:8000/accounts/signup]()
- logout
> [localhost:8000/accounts/logout]()
###### profile pages
> Filling the relative user informations is a must to access Discount's index page.
- Student profile
> [localhost:8000/accounts/info/stu]()
- Parent profile
> [localhost:8000/accounts/info/par]()
- School profile
> [localhost:8000/accounts/info/sch]()
- Operator profile
> [localhost:8000/accounts/info/opr]()
###### Discount pages
- Discount Creation (The users who fill thier profile information have access)
> [localhost:8000]()
- Using Discount (Student users who fill their profile have access)
> [localhost:8000/use]()
- Report Discounts (Staff Users have access)
> [localhost:8000/report]()
- Users used a specific percent discount, mentioned by code.
> [localhost:8000/percent/code/users]()
- Users used a specific amount discount, mentioned by code.
> [localhost:8000/amount/code/users]()

