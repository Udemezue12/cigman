import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
app = Celery('portfolio_project')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


