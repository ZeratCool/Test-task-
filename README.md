# CREATE ENVIROMENT:

``python -m venv venv`` 

# INSTALL Packeges:

``pip install -r requirements.txt``

# Config .docker.env file :
```
SECRET_KEY=""
DEBUG=""

#DB
DB_NAME=""
DB_USER=""
PSW=""
HOST=""
PORT=""

```

## How to run the system:
# 1.Clone code

# 2.Go to application root folder: "/lunch_service"

# 3. Create .env file with your Django secret key(SECRET_KEY=<your secret key>)
Run`` "sudo docker-compose up"``
CREATE POSTGRES DATABASE: 


## If run localy
```
sudo -u postgres psql
======================

CREATE DATABASE my project;
CREATE USER postgres WITH PASSWORD 'postgres';

ALTER ROLE lunch_service_user SET client_encoding TO 'utf8';
ALTER ROLE lunch_service_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE lunch_service_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE lunch_service TO lunch_service_user;

\q
```

CREATE SUPER USER :

``make superuser
``

Do migration:

`` make migrate``

Start app :

``make run``
