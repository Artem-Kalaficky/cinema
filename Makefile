MANAGE = python manage.py

run:
	$(MANAGE) runserver

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

worker:
	celery -A cinema worker --loglevel=info

startapp:
	$(MANAGE) migrate --no-input
	$(MANAGE) loaddata db.json
	$(MANAGE) compilemessages
    gunicorn cinema.wsgi:application --bind 0.0.0.0:8000

