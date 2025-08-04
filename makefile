# Makefile

# Variables (opcional)
DC = docker compose
WEB = web

.PHONY: up down build logs migrate shell createsuperuser loaddata


runserver:
	@$(DC) stop web 
	@$(DC) run --rm --service-ports web \
	python manage.py runserver 0.0.0.0:8000



up:
	$(DC) up -d

down:
	$(DC) down -v

build:
	$(DC) build

logs:
	$(DC) logs -f

migrate:
	$(DC) exec $(WEB) python manage.py migrate

createsuperuser:
	$(DC) exec $(WEB) python manage.py createsuperuser

shell:
	$(DC) exec $(WEB) python manage.py shell

loaddata:
	$(DC) cp data.json $(WEB):/app/data.json
	$(DC) exec $(WEB) python manage.py loaddata data.json


