from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# indica el módulo de settings de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thesis.settings')

# crea la instancia de Celery
app = Celery('thesis')

# lee la configuración de CELERY_* en settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto-descubre tasks.py en cada app INSTALLED_APPS
app.autodiscover_tasks()