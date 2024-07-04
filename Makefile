migrate:
	python lunch_service/manage.py makemigrations
	python lunch_service/manage.py migrate
run:
	python lunch_service/manage.py runserver

superuser:
	python lunch_service/manage.py createsuperuser
