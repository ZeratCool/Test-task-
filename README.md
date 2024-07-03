CREATE ENVIROMENT:

``python -m venv venv`` 

INSTALL Packeges:

``pip install -r requirements.txt``

CREATE POSTGRES DATABASE: 

```
sudo -u postgres psql
======================

CREATE DATABASE lunch_service;
CREATE USER lunch_service_user WITH PASSWORD 'password';

ALTER ROLE lunch_service_user SET client_encoding TO 'utf8';
ALTER ROLE lunch_service_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE lunch_service_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE lunch_service TO lunch_service_user;

\q
```
CHANGE settings.py:
```
. . .

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env('DB_NAME'),
        "USER": env('DB_USER'),
        "PASSWORD": env('PSW'),
        "HOST": env('HOST'),
        "PORT": env('PORT'),
    }
}

. . .
```
CREATE SUPER USER :

``make superuser
``

Do migration:

`` make migrate``

Start app :

``make run``
