__author__ = 'Pareng Je'
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'micpschool.settings')

app = Celery('micpschool')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
