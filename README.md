# TASK:



## Config .docker.env file :
```
SECRET_KEY=""
DEBUG=""   #default=False 
 
#DB # add this only if you run localy
DB_NAME=""
DB_USER=""
DB_PASSWORD=""
DB_HOST=""
DB_PORT=""

```

## How to run the system:
 1.Clone code
 2.Go to application root folder: "/lunch_service"

 3.Run`` "sudo docker-compose up"``
 4. link to web app by this: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
 
#CREATE POSTGRES DATABASE:   

```
#Do it only if you run localy#
 
sudo -u postgres psql
======================

CREATE DATABASE my_project;
CREATE USER myuser WITH PASSWORD 'postgres';

ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE my_project TO myuser;

\q
```

CREATE SUPER USER :
```
make superuser
#IF use Docker:
sudo docker exec -it &lt;name from first paragraph&gt;
make superuser
```
**Important that for Authentication use email and password** 



## All API manipulation works only by JWT(JSON Web Token)

1.Register users with privileges or none: ``account/register/`` 

2.Create restaurant: ``api/restaurants/add``

3.Update restaurant: ``api/restaurant/<ID_RESTAURANT>/update/``

4.Add menu : ``api/add_menu`` 


# Run tests:

1.Virtual enviroment
```
python -m venv venv
sourse/venv/bin/activate
```

2.Go to main folder ``cd ./lunch_service``

3. Config .env file

4. ``pip install -r requirements.txt``

5. Go to test folder: ``cd /tests/``

6. Run ``pytest``
